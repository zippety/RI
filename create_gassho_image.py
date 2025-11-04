"""
Create a Gassho image using Nano Banana or Python drawing
Generates a simple, clear Gassho (prayer position) image
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Image dimensions
WIDTH = 800
HEIGHT = 1000
DPI = 300

def create_gassho_image_simple():
    """Create a simple Gassho image using Python/PIL"""
    # Create image with white background
    img = Image.new('RGB', (WIDTH, HEIGHT), '#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    # Colors
    SKIN_COLOR = '#F5E6D3'
    OUTLINE_COLOR = '#333333'
    BG_COLOR = '#FFFFFF'
    
    # Center coordinates
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    # Draw a simple person figure showing Gassho position
    # Head
    head_radius = 60
    head_y = center_y - 200
    draw.ellipse(
        [center_x - head_radius, head_y - head_radius,
         center_x + head_radius, head_y + head_radius],
        fill=SKIN_COLOR, outline=OUTLINE_COLOR, width=2
    )
    
    # Body/torso
    body_width = 120
    body_height = 180
    body_y = head_y + head_radius
    draw.rectangle(
        [center_x - body_width//2, body_y,
         center_x + body_width//2, body_y + body_height],
        fill='#E5F0FF', outline=OUTLINE_COLOR, width=2
    )
    
    # Arms (bent to center for Gassho)
    arm_length = 80
    elbow_bend = 40
    
    # Left arm (from viewer's perspective, right side)
    left_shoulder_x = center_x - body_width//2
    left_elbow_x = center_x - elbow_bend
    left_wrist_x = center_x - 15
    
    # Left upper arm
    draw.line(
        [(left_shoulder_x, body_y + 20), (left_elbow_x, body_y + 60)],
        fill=SKIN_COLOR, width=20
    )
    # Left forearm
    draw.line(
        [(left_elbow_x, body_y + 60), (left_wrist_x, center_y)],
        fill=SKIN_COLOR, width=20
    )
    
    # Right arm
    right_shoulder_x = center_x + body_width//2
    right_elbow_x = center_x + elbow_bend
    right_wrist_x = center_x + 15
    
    # Right upper arm
    draw.line(
        [(right_shoulder_x, body_y + 20), (right_elbow_x, body_y + 60)],
        fill=SKIN_COLOR, width=20
    )
    # Right forearm
    draw.line(
        [(right_elbow_x, body_y + 60), (right_wrist_x, center_y)],
        fill=SKIN_COLOR, width=20
    )
    
    # HANDS TOGETHER (Gassho position) - at heart center
    hand_width = 50
    hand_height = 80
    
    # Left hand (palm facing right)
    left_hand_x = center_x - hand_width * 0.6
    draw.ellipse(
        [left_hand_x - hand_width//2, center_y - hand_height//2,
         left_hand_x + hand_width//2, center_y + hand_height//2],
        fill=SKIN_COLOR, outline='#4A90E2', width=4
    )
    
    # Right hand (palm facing left, touching left hand)
    right_hand_x = center_x + hand_width * 0.6
    draw.ellipse(
        [right_hand_x - hand_width//2, center_y - hand_height//2,
         right_hand_x + hand_width//2, center_y + hand_height//2],
        fill=SKIN_COLOR, outline='#4A90E2', width=4
    )
    
    # Fingers pointing UP (lines extending upward)
    finger_length = hand_height * 0.4
    finger_y_start = center_y - hand_height//2 + 10
    finger_y_end = finger_y_start - finger_length
    
    # Draw 4 fingers on each hand
    for i in range(4):
        finger_offset = (i - 1.5) * hand_width * 0.25
        # Left hand fingers
        draw.line(
            [(left_hand_x + finger_offset, finger_y_start),
             (left_hand_x + finger_offset, finger_y_end)],
            fill='#4A90E2', width=4
        )
        # Right hand fingers
        draw.line(
            [(right_hand_x + finger_offset, finger_y_start),
             (right_hand_x + finger_offset, finger_y_end)],
            fill='#4A90E2', width=4
        )
    
    # Connection line between hands (they're touching)
    draw.line(
        [(left_hand_x + hand_width//2, center_y),
         (right_hand_x - hand_width//2, center_y)],
        fill='#4A90E2', width=6
    )
    
    # Label at bottom
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    label = "GASSHO"
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    x = (WIDTH - text_width) // 2
    draw.text((x, HEIGHT - 80), label, fill='#4A90E2', font=font)
    
    # Save
    output_path = os.path.join(BASE_DIR, "01_Images", "Gassho", "gassho_created.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', dpi=(DPI, DPI))
    print(f"Created Gassho image: {output_path}")
    return output_path

# For Nano Banana API (if available)
def create_gassho_nano_banana():
    """Create Gassho image using Nano Banana API (if available)"""
    # Note: This would require Nano Banana API access
    # For now, this is a placeholder
    
    prompt = """
    Create a clear, educational image showing the Gassho hand position:
    - Two hands pressed together in prayer position
    - Fingers pointing upward
    - Palms touching at heart center
    - Simple, clean background
    - Educational style, suitable for teaching materials
    - Clear and easy to understand
    """
    
    print("Nano Banana prompt:")
    print(prompt)
    print("\nTo use Nano Banana:")
    print("1. Visit https://www.bananaimages.com/ or Nano Banana platform")
    print("2. Use the prompt above")
    print("3. Generate the image")
    print("4. Download and save to 01_Images/Gassho/ folder")
    
    return None

if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    BASE_DIR = Path(__file__).parent
    
    print("Creating Gassho image...")
    print("\nOptions:")
    print("1. Create simple Gassho image using Python (default)")
    print("2. Generate prompt for Nano Banana")
    
    # Create simple image
    output_path = create_gassho_image_simple()
    
    # Also show Nano Banana prompt
    print("\n" + "="*60)
    create_gassho_nano_banana()
    
    print(f"\nGassho image created: {output_path}")
    print("\nNext steps:")
    print("1. Review the image")
    print("2. Update 01_Images/Gassho/README.md with attribution")
    print("3. Commit to GitHub")

