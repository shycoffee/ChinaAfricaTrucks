#!/usr/bin/env python3
"""
通亚官网图片下载脚本
使用方法:
1. 安装依赖: pip install requests beautifulsoup4
2. 运行: python download_images.py
"""

import os
import requests
from urllib.parse import urljoin

# 创建图片目录
os.makedirs('assets/images', exist_ok=True)

# 通亚官网图片URL列表 (从浏览器获取)
image_urls = [
    # 工厂图片
    "http://www.chinatongya.com/uploads/image/20230801/1690873620.jpg",
    
    # 产品图片
    "http://www.chinatongya.com/uploads/image/20260210/1770694088.jpg",  # 后翻自卸半挂车
    "http://www.chinatongya.com/uploads/image/20260210/1770695275.jpg",
    "http://www.chinatongya.com/uploads/image/20260210/1770700091.jpg",
    "http://www.chinatongya.com/uploads/image/20260210/1770691902.jpg",
    "http://www.chinatongya.com/uploads/image/20260210/1770697755.jpg",
    "http://www.chinatongya.com/uploads/image/20260210/1770690654.jpg",
    
    # Logo
    "http://www.chinatongya.com/uploads/image/20161021/1477034941.png",
    "http://www.chinatongya.com/images/tongya2logo.png",
]

# 对应的文件名
filenames = [
    "tongya-factory.jpg",
    "dump-trailer-1.jpg",
    "dump-trailer-2.jpg",
    "dump-trailer-3.jpg",
    "dump-trailer-4.jpg",
    "dump-trailer-5.jpg",
    "dump-trailer-6.jpg",
    "tongya-logo-1.png",
    "tongya-logo-2.png",
]

def download_image(url, filename):
    """下载单个图片"""
    try:
        print(f"正在下载: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        filepath = os.path.join('assets/images', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ 已保存: {filepath} ({len(response.content)} bytes)")
        return True
        
    except Exception as e:
        print(f"✗ 下载失败: {url}")
        print(f"  错误: {e}")
        return False

def main():
    print("开始下载通亚官网图片...")
    print(f"目标目录: {os.path.abspath('assets/images')}")
    print("-" * 50)
    
    success_count = 0
    for url, filename in zip(image_urls, filenames):
        if download_image(url, filename):
            success_count += 1
    
    print("-" * 50)
    print(f"下载完成: {success_count}/{len(image_urls)} 个图片")
    
    if success_count > 0:
        print("\n下一步:")
        print("1. 使用 TinyPNG (https://tinypng.com) 压缩图片")
        print("2. 修改HTML文件引用本地图片")
        print("3. 推送到GitHub")
    else:
        print("\n所有下载都失败了，请检查网络连接或手动下载图片。")

if __name__ == "__main__":
    main()