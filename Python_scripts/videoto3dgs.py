import os
import subprocess

def extract_frames(
    video_path,
    output_dir="frames",
    fps=10,
    image_format="png"
):

    # Check if video exists
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # FFmpeg command
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps={fps}",
        os.path.join(output_dir, f"frame_%04d.{image_format}")
    ]

    print("Running FFmpeg command:")
    print(" ".join(command))

    # Run command
    subprocess.run(command, check=True)

    print(f"\nFrames extracted successfully to '{output_dir}'")


if __name__ == "__main__":
    VIDEO_PATH = "dukemon_hybrid.mp4"   
    OUTPUT_DIR = "images_dukemon"            
    FPS = 25                           
    extract_frames(
        video_path=VIDEO_PATH,
        output_dir=OUTPUT_DIR,
        fps=FPS,
        image_format="png"
    )
