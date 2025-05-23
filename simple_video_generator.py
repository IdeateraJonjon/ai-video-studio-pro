#!/usr/bin/env python3
"""
Simple AI Video Generator
Uses Text2Video-Zero pipeline for generating videos from text prompts
"""

import torch
from diffusers import TextToVideoZeroPipeline
import os
from datetime import datetime

def generate_video(prompt, output_dir="outputs", duration=3, fps=8):
    """
    Generate a video from a text prompt
    
    Args:
        prompt (str): Text description of the video
        output_dir (str): Directory to save the video
        duration (int): Duration in seconds
        fps (int): Frames per second
    """
    
    print(f"🎬 Starting video generation...")
    print(f"📝 Prompt: {prompt}")
    print(f"⏱️  Duration: {duration}s at {fps} FPS")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the pipeline
    print("🔄 Loading AI model (this may take a few minutes on first run)...")
    
    try:
        # Use CPU since no CUDA available
        device = "cpu"
        torch_dtype = torch.float32
        
        pipe = TextToVideoZeroPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch_dtype
        ).to(device)
        
        print("✅ Model loaded successfully!")
        
        # Generate video
        print("🎥 Generating video...")
        
        num_frames = duration * fps
        video_frames = pipe(
            prompt=prompt,
            video_length=num_frames,
            num_inference_steps=20,  # Lower for faster generation
            guidance_scale=7.5,
            width=512,
            height=512
        ).frames
        
        # Save video
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"video_{timestamp}.mp4")
        
        # Convert frames to video using moviepy
        from moviepy.editor import ImageSequenceClip
        
        clip = ImageSequenceClip(video_frames, fps=fps)
        clip.write_videofile(output_path, codec='libx264')
        
        print(f"✅ Video saved to: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ Error generating video: {str(e)}")
        print("💡 Try installing dependencies: pip install diffusers transformers torch moviepy")
        return None

def batch_generate_scenes(scenes_file, output_dir="outputs"):
    """
    Generate multiple videos from a file containing scene descriptions
    """
    
    if not os.path.exists(scenes_file):
        print(f"❌ Scenes file not found: {scenes_file}")
        return
    
    with open(scenes_file, 'r', encoding='utf-8') as f:
        scenes = f.read().strip().split('\n\n')
    
    print(f"🎬 Found {len(scenes)} scenes to generate")
    
    generated_videos = []
    for i, scene in enumerate(scenes, 1):
        if scene.strip():
            print(f"\n🎥 Generating scene {i}/{len(scenes)}")
            video_path = generate_video(
                prompt=scene.strip(),
                output_dir=output_dir,
                duration=6  # 6 seconds per scene
            )
            if video_path:
                generated_videos.append(video_path)
    
    print(f"\n✅ Generated {len(generated_videos)} videos!")
    return generated_videos

if __name__ == "__main__":
    # Example usage
    print("🌊 Ocean Pollution Video Generator")
    print("=" * 50)
    
    # Test with a simple scene
    test_prompt = "Cinematic aerial shot of pristine turquoise ocean at golden hour sunrise, crystal clear waters, gentle waves sparkling in morning light"
    
    print("🧪 Testing with sample prompt...")
    generate_video(test_prompt, duration=3)
