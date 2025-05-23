"""
Simple Test - Generate one ocean scene
"""
import os
os.system("pip install diffusers torch transformers pillow")

try:
    from diffusers import StableDiffusionPipeline
    import torch
    
    print("🌊 Testing Ocean Video Generation...")
    
    # Simple test
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )
    
    prompt = "pristine blue ocean aerial view sunrise cinematic"
    image = pipe(prompt, num_inference_steps=10).images[0]
    
    os.makedirs("test_output", exist_ok=True)
    image.save("test_output/ocean_test.png")
    
    print("✅ Test successful! Check test_output/ocean_test.png")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("🔧 Try manual installation:")
    print("pip install --upgrade torch torchvision")
    print("pip install diffusers transformers accelerate")
