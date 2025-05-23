"""
Batch Ocean Video Generator
Generates all 9 scenes from the ocean pollution script
"""

def generate_all_scenes():
    """Generate all ocean pollution scenes"""
    
    # Import after ensuring dependencies are installed
    try:
        from diffusers import DiffusionPipeline
        import torch
        import os
        
        print("🌊 OCEAN POLLUTION VIDEO GENERATOR")
        print("=" * 50)
        print("⚠️  First run will download ~7GB model - please be patient!")
        print("💻 Running on CPU - each scene takes 10-20 minutes")
        print()
        
        # Setup
        device = "cpu"
        output_dir = "ocean_videos"
        os.makedirs(output_dir, exist_ok=True)
        
        # Scene prompts (6 seconds each)
        scenes = [
            "Pristine turquoise ocean at sunrise, aerial view, crystal clear water",
            "Plastic bottles falling like rain into ocean, environmental disaster",
            "Underwater view of plastic debris cloud, pollution in clear water",
            "Garbage trucks dumping plastic waste, industrial documentary style",
            "Aerial view Great Pacific Garbage Patch, massive plastic vortex",
            "Sea turtle entangled in plastic nets, struggling underwater",
            "City to ocean pollution flow, fast montage of consumption to waste",
            "Split screen pristine vs polluted ocean, before and after comparison",
            "Earth from space showing garbage patches, environmental overview"
        ]
        
        print(f"🎬 Will generate {len(scenes)} scenes...")
        
        # Simple generation using Stable Diffusion Video
        for i, prompt in enumerate(scenes, 1):
            print(f"\n🎥 Generating Scene {i}/{len(scenes)}")
            print(f"📝 {prompt}")
            
            try:
                # Use a simpler approach - generate image sequence
                from diffusers import StableDiffusionPipeline
                
                pipe = StableDiffusionPipeline.from_pretrained(
                    "runwayml/stable-diffusion-v1-5",
                    torch_dtype=torch.float32
                )
                pipe = pipe.to(device)
                
                # Generate multiple frames for video effect
                frames = []
                for frame_num in range(24):  # 3 seconds at 8fps
                    modified_prompt = f"{prompt}, frame {frame_num}, cinematic"
                    image = pipe(modified_prompt, num_inference_steps=20).images[0]
                    frames.append(image)
                
                # Save as image sequence (you can convert to video later)
                scene_dir = os.path.join(output_dir, f"scene_{i:02d}")
                os.makedirs(scene_dir, exist_ok=True)
                
                for j, frame in enumerate(frames):
                    frame.save(os.path.join(scene_dir, f"frame_{j:03d}.png"))
                
                print(f"✅ Scene {i} saved to {scene_dir}")
                
            except Exception as e:
                print(f"❌ Error generating scene {i}: {e}")
        
        print("\n🎉 All scenes generated!")
        print(f"📁 Check the '{output_dir}' folder")
        print("💡 Use video editing software to combine frames into videos")
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("🔧 Run: pip install diffusers torch transformers")

if __name__ == "__main__":
    generate_all_scenes()
