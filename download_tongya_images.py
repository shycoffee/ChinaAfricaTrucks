#!/usr/bin/env python3
"""
直接下载通亚官网图片脚本
"""

import os
import requests
import time

# 创建图片目录
os.makedirs('assets/images', exist_ok=True)

# 通亚官网图片URL列表 (从浏览器分析获得)
image_urls = [
    # 1. 工厂图片 - 最重要
    ("http://www.chinatongya.com/uploads/image/20230801/1690873620.jpg", "tongya-factory.jpg"),
    
    # 2. 产品图片 - 自卸车 (后翻自卸半挂车)
    ("http://www.chinatongya.com/uploads/image/20260210/1770694088.jpg", "dump-trailer-1.jpg"),
    ("http://www.chinatongya.com/uploads/image/20260210/1770695275.jpg", "dump-trailer-2.jpg"),
    ("http://www.chinatongya.com/uploads/image/20260210/1770700091.jpg", "dump-trailer-3.jpg"),
    
    # 3. 更多产品角度
    ("http://www.chinatongya.com/uploads/image/20260210/1770691902.jpg", "dump-trailer-4.jpg"),
    ("http://www.chinatongya.com/uploads/image/20260210/1770697755.jpg", "dump-trailer-5.jpg"),
    ("http://www.chinatongya.com/uploads/image/20260210/1770690654.jpg", "dump-trailer-6.jpg"),
    
    # 4. 细节图片
    ("http://www.chinatongya.com/uploads/image/20260210/1770691001.jpg", "detail-1.jpg"),
    ("http://www.chinatongya.com/uploads/image/20260210/1770696156.jpg", "detail-2.jpg"),
    
    # 5. Logo
    ("http://www.chinatongya.com/uploads/image/20161021/1477034941.png", "tongya-logo.png"),
]

def download_image(url, filename):
    """下载单个图片"""
    try:
        print(f"正在下载: {filename}")
        
        # 设置请求头，模拟浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'http://www.chinatongya.com/',
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        filepath = os.path.join('assets/images', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        file_size = len(response.content) / 1024  # KB
        print(f"✓ 已保存: {filepath} ({file_size:.1f} KB)")
        return True
        
    except Exception as e:
        print(f"✗ 下载失败 {filename}: {e}")
        return False

def main():
    print("开始下载通亚官网图片...")
    print(f"目标目录: {os.path.abspath('assets/images')}")
    print("-" * 50)
    
    success_count = 0
    for url, filename in image_urls:
        if download_image(url, filename):
            success_count += 1
        time.sleep(1)  # 礼貌延迟
    
    print("-" * 50)
    print(f"下载完成: {success_count}/{len(image_urls)} 个图片")
    
    if success_count > 0:
        print("\n✅ 下载的图片:")
        for _, filename in image_urls:
            filepath = os.path.join('assets/images', filename)
            if os.path.exists(filepath):
                size = os.path.getsize(filepath) / 1024
                print(f"  • {filename} ({size:.1f} KB)")
        
        print("\n🚀 下一步:")
        print("1. 检查下载的图片")
        print("2. 修改HTML文件引用本地图片")
        print("3. 推送到GitHub")
    else:
        print("\n❌ 所有下载都失败了")
        print("请尝试:")
        print("1. 检查网络连接")
        print("2. 手动访问 http://www.chinatongya.com 下载图片")
        print("3. 右键保存图片到 assets/images/ 文件夹")

if __name__ == "__main__":
    main()