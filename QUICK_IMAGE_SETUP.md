# 🚀 快速图片设置指南

## 问题分析

**为什么之前无法访问通亚官网图片？**
1. `web_extract` 工具被安全策略阻止，认为 `www.chinatongya.com` 是"私有或内部网络地址"
2. 浏览器工具可以正常访问，因为使用不同的网络环境
3. 图片URL是公开可访问的

## ✅ 解决方案

### 方案A: 直接使用图片URL (最简单)

直接修改HTML，使用通亚官网的图片URL：

```html
<!-- 在 factories/tongya.html 中 -->
<!-- 替换工厂主图 (第156-160行) -->
<div class="factory-hero-image">
    <img src="http://www.chinatongya.com/uploads/image/20230801/1690873620.jpg" 
         alt="Tongya Heavy Industry Factory" 
         style="width: 100%; height: 100%; object-fit: cover; border-radius: 1rem;">
</div>

<!-- 替换产品图片 (示例) -->
<div class="product-image">
    <span class="product-badge">Hot Sale</span>
    <img src="http://www.chinatongya.com/uploads/image/20260210/1770694088.jpg" 
         alt="40ft Flatbed Trailer" loading="lazy">
</div>
```

**优点**: 无需下载，立即生效
**缺点**: 依赖通亚服务器

### 方案B: 使用脚本下载 (推荐)

1. **运行下载脚本**:
```bash
cd /Users/alan/Work/trailer-matrix/website-v2
python3 download_images.py
```

2. **如果缺少依赖**:
```bash
pip install requests beautifulsoup4
```

3. **压缩图片** (使用 https://tinypng.com):
   - 上传下载的图片
   - 下载压缩后的版本
   - 替换原文件

### 方案C: 手动下载 (最可靠)

1. **访问通亚官网**: http://www.chinatongya.com
2. **导航到产品页面**: 点击"产品世界" → "半挂车系列"
3. **右键保存图片**:
   - 在图片上右键 → "图片另存为..."
   - 保存到 `assets/images/` 文件夹

---

## 📸 核心图片清单

### 必须下载的图片 (5张)

| 用途 | 建议文件名 | 通亚官网图片 |
|------|------------|--------------|
| 工厂主图 | `tongya-factory.jpg` | http://www.chinatongya.com/uploads/image/20230801/1690873620.jpg |
| 平板挂车 | `flatbed-40ft.jpg` | 需要从产品页面找 |
| 低平板挂车 | `lowbed-60ton.jpg` | 需要从产品页面找 |
| 油罐车 | `tanker-45000l.jpg` | 需要从产品页面找 |
| 自卸车 | `dump-rear.jpg` | http://www.chinatongya.com/uploads/image/20260210/1770694088.jpg |

### 可选图片
- 工厂Logo: `tongya-logo.png`
- 更多产品角度图片
- 工厂车间图片

---

## 🛠️ 修改HTML代码

### 1. 首页修改 (index.html)

**原代码** (第143-148行):
```html
<div class="factory-image">
    <div class="factory-badge">Exclusive Partner</div>
    <div class="factory-placeholder">
        <i class="fas fa-industry"></i>
    </div>
</div>
```

**修改为** (使用本地图片):
```html
<div class="factory-image">
    <div class="factory-badge">Exclusive Partner</div>
    <img src="assets/images/tongya-factory.jpg" alt="Tongya Heavy Industry Factory" loading="lazy">
</div>
```

**或** (使用远程URL):
```html
<div class="factory-image">
    <div class="factory-badge">Exclusive Partner</div>
    <img src="http://www.chinatongya.com/uploads/image/20230801/1690873620.jpg" alt="Tongya Heavy Industry Factory" loading="lazy">
</div>
```

### 2. 工厂页面修改 (factories/tongya.html)

**工厂主图** (第156-160行):
```html
<!-- 原代码 -->
<div class="factory-hero-image">
    <i class="fas fa-industry"></i>
    <p style="margin-top: 1rem; opacity: 0.7;">Factory Photo Placeholder</p>
</div>

<!-- 修改为 -->
<div class="factory-hero-image">
    <img src="../assets/images/tongya-factory.jpg" alt="Tongya Heavy Industry Factory" style="width: 100%; height: 100%; object-fit: cover; border-radius: 1rem;">
</div>
```

**产品图片** (示例: 第201-206行):
```html
<!-- 原代码 -->
<div class="product-image">
    <span class="product-badge">Hot Sale</span>
    <div class="placeholder">
        <i class="fas fa-truck-flatbed"></i>
    </div>
</div>

<!-- 修改为 -->
<div class="product-image">
    <span class="product-badge">Hot Sale</span>
    <img src="../assets/images/flatbed-40ft.jpg" alt="40ft Flatbed Trailer" loading="lazy">
</div>
```

---

## ⚡ 快速启动步骤

### 步骤1: 创建图片目录
```bash
mkdir -p /Users/alan/Work/trailer-matrix/website-v2/assets/images
```

### 步骤2: 下载至少1张图片
从通亚官网下载 `tongya-factory.jpg` 或使用提供的URL

### 步骤3: 修改首页图片引用
编辑 `index.html`，替换通亚工厂卡片的图片

### 步骤4: 测试
访问 https://chinaafricatrucks.com 查看效果

### 步骤5: 逐步完善
- 下载更多产品图片
- 更新工厂页面
- 压缩图片优化加载速度

---

## 🔧 技术细节

### 图片URL分析
通亚官网图片URL模式:
```
http://www.chinatongya.com/uploads/image/{日期}/{时间戳}.jpg
```

### 防盗链处理
如果遇到防盗链问题，可以:
1. 下载图片到本地
2. 使用CDN服务
3. 联系通亚获取授权

### 性能优化
- **尺寸**: 1200x800px 足够
- **格式**: JPG (照片), PNG (Logo)
- **压缩**: 使用 TinyPNG 压缩到 < 200KB
- **懒加载**: 已配置 `loading="lazy"`

---

## 🎯 立即行动建议

### 最低可行方案 (今天完成)
1. 下载1张工厂图片
2. 更新首页通亚卡片
3. 推送到GitHub

### 完整方案 (本周完成)
1. 下载5张核心图片
2. 更新所有产品卡片
3. 完善工厂页面图库
4. 优化图片加载

---

## 📞 需要帮助？

如果遇到问题:
1. **网络问题**: 尝试使用VPN访问通亚官网
2. **下载失败**: 手动右键保存图片
3. **代码修改**: 我可以帮你修改HTML
4. **部署问题**: 检查GitHub Pages设置

**现在可以开始下载图片了！** 🚀