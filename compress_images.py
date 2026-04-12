#!/usr/bin/env python3
"""
图片压缩脚本 - 使用PIL/Pillow
"""

import os
from PIL import Image
import glob

def compress_image(input_path, output_path, quality=85, max_size=(1200, 800)):
    """压缩图片"""
    try:
        with Image.open(input_path) as img:
            # 转换模式
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # 调整尺寸
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # 保存
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            original_size = os.path.getsize(input_path) / 1024
            new_size = os.path.getsize(output_path) / 1024
            reduction = (1 - new_size / original_size) * 100
            
            print(f"✓ {os.path.basename(input_path)}: {original_size:.1f}KB → {new_size:.1f}KB (-{reduction:.1f}%)")
            return True
            
    except Exception as e:
        print(f"✗ 压缩失败 {input_path}: {e}")
        return False

def main():
    print("开始压缩图片...")
    
    # 需要压缩的图片
    images_to_compress = [
        'dump-trailer-1.jpg',
        'dump-trailer-2.jpg', 
        'dump-trailer-3.jpg',
        'dump-trailer-4.jpg',
        'dump-trailer-5.jpg',
        'dump-trailer-6.jpg',
        'tongya-factory.jpg',
    ]
    
    success_count = 0
    for filename in images_to_compress:
        input_path = os.path.join('assets/images', filename)
        if os.path.exists(input_path):
            if compress_image(input_path, input_path, quality=80):
                success_count += 1
    
    print(f"\n压缩完成: {success_count}/{len(images_to_compress)} 个图片")
    
    # 显示最终大小
    print("\n📊 最终图片大小:")
    for filename in os.listdir('assets/images'):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join('assets/images', filename)
            size = os.path.getsize(path) / 1024
            print(f"  • {filename}: {size:.1f} KB")

if __name__ == "__main__":
    main()