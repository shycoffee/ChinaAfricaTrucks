# China Africa Trucks - Professional Export Platform

A modern, bilingual (English/Chinese) website for China Africa Trucks - connecting African businesses with certified Chinese truck and trailer manufacturers.

## 🌐 Live Website

**Production URL**: https://chinaafricatrucks.com

**GitHub Pages URL**: https://shycoffee.github.io/ChinaAfricaTrucks

## ✨ Features

### Core Features
- **Bilingual Support**: Full English and Chinese language switching
- **Matrix Architecture**: Multiple factory partners (not just Tongya)
- **Product Categories**: 6 main categories with sub-products
- **Modern Design**: Clean, professional, mobile-first responsive design
- **Performance Optimized**: Fast loading, lazy loading images
- **SEO Ready**: Meta tags, semantic HTML, structured data

### Technical Features
- **Static Site**: No server required, hosted on GitHub Pages
- **Custom Domain**: Professional domain with HTTPS
- **Contact Integration**: WhatsApp, email, and contact form
- **Animations**: Smooth scroll, intersection observer animations
- **Mobile Optimized**: Perfect for African mobile users

## 🏗️ Website Architecture

### Multi-Factory Matrix
This website represents a **platform approach** rather than a single factory:

1. **Tongya Heavy Industry** - Featured partner (Liangshan, Shandong)
2. **Sinotruk Group** - Heavy duty trucks (Jinan, Shandong)
3. **Xiamen Trailer Tech** - Specialized trailers (Xiamen, Fujian)
4. **More factories** - Can be added dynamically

### Product Categories
1. **Flatbed Trailers** - 20ft, 40ft, 45ft container trailers
2. **Lowbed Trailers** - Heavy equipment transport
3. **Tanker Trailers** - Fuel, chemical, food-grade
4. **Dump Trailers** - Rear, side, end dump
5. **Cargo Trucks** - Light, medium, heavy duty
6. **Tractor Heads** - 4x2, 6x4, 6x2 configurations

### Export Markets
- Nigeria (Lagos, Abuja, Kano)
- Kenya (Nairobi, Mombasa)
- Ghana (Accra, Tema)
- Tanzania (Dar es Salaam)
- Uganda (Kampala)
- Zambia
- South Africa
- Ethiopia

## 🛠️ Technology Stack

- **HTML5**: Semantic markup
- **CSS3**: Modern Grid, Flexbox, Custom Properties
- **JavaScript (ES6+)**: Vanilla JS, no frameworks
- **Internationalization**: JSON-based translation system
- **Hosting**: GitHub Pages
- **Domain**: GoDaddy with custom DNS

## 📁 Project Structure

```
website-v2/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Main stylesheet (27KB)
├── js/
│   ├── i18n.js         # Internationalization module
│   └── main.js         # Main JavaScript functionality
├── lang/
│   ├── en.json         # English translations
│   └── zh.json         # Chinese translations
├── assets/
│   ├── images/         # Image assets (to be added)
│   └── fonts/          # Custom fonts (if needed)
├── CNAME               # Custom domain configuration
└── README.md           # This file
```

## 🚀 Deployment

### Step 1: Push to GitHub

```bash
cd website-v2

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial launch: Bilingual matrix platform website"

# Add remote (replace with your repo)
git remote add origin git@github.com:shycoffee/ChinaAfricaTrucks.git

# Push to main branch
git push -u origin main --force
```

### Step 2: Enable GitHub Pages

1. Go to: https://github.com/shycoffee/ChinaAfricaTrucks/settings/pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Click Save
5. Wait 2-3 minutes for deployment

### Step 3: Configure GoDaddy DNS

Add these DNS records in GoDaddy:

**A Records** (4 total):
```
Type: A | Name: @ | Value: 185.199.108.153 | TTL: 1 Hour
Type: A | Name: @ | Value: 185.199.109.153 | TTL: 1 Hour
Type: A | Name: @ | Value: 185.199.110.153 | TTL: 1 Hour
Type: A | Name: @ | Value: 185.199.111.153 | TTL: 1 Hour
```

**CNAME Record**:
```
Type: CNAME | Name: www | Value: shycoffee.github.io | TTL: 1 Hour
```

### Step 4: Enable HTTPS

1. In GitHub repository, go to Settings → Pages
2. Check "Enforce HTTPS"
3. Wait for SSL certificate (5-30 minutes)

## 📝 Content Management

### Adding a New Factory

1. Copy an existing factory card in `index.html`
2. Update:
   - Factory name
   - Location
   - Specialty
   - Description
   - Certifications
   - Links

### Adding a New Product Category

1. Add to the categories grid in `index.html`
2. Update translations in `lang/en.json` and `lang/zh.json`
3. Add corresponding factory products

### Updating Translations

Edit `lang/en.json` or `lang/zh.json`:

```json
{
  "key": {
    "nested": "Translation text"
  }
}
```

Reference in HTML:
```html
<span data-i18n="key.nested">Default text</span>
```

## 🎨 Design System

### Colors
- Primary: `#1e40af` (Blue)
- Secondary: `#f59e0b` (Amber)
- Accent: `#10b981` (Green)
- WhatsApp: `#25d366`
- Text Dark: `#0f172a`
- Text Body: `#334155`
- Text Light: `#64748b`

### Typography
- Font Family: Inter (Google Fonts)
- Headings: 700 weight
- Body: 400 weight
- Base Size: 16px

### Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 📱 Mobile Optimization

The website is optimized for African mobile users:

- Touch-friendly buttons (min 44px)
- Fast loading on 3G networks
- WhatsApp integration for common communication
- Mobile-first CSS approach
- Responsive images

## 🔍 SEO Configuration

### Meta Tags (Already configured)
- Title: Dynamic per page
- Description: Optimized for keywords
- Keywords: China trucks, Africa export, trailers
- Open Graph: Social media sharing

### To Add Later
- Google Analytics tracking code
- Google Search Console verification
- Sitemap.xml
- robots.txt

## 📞 Contact Information

Integrated in website:
- **WhatsApp**: +234 814 006 7523
- **Email**: chinaafricatrucks@gmail.com
- **TikTok**: @ChinaAfricaTrucks
- **Office**: Liangshan, Shandong, China

## 🔧 Customization Guide

### Change WhatsApp Number
Edit in `index.html`:
```html
<a href="https://wa.me/YOUR_NUMBER">
```

### Change Email
Edit in `index.html`:
```html
<a href="mailto:your@email.com">
```

### Add Google Analytics
Add to `<head>` in `index.html`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_GA_ID');
</script>
```

### Configure Contact Form
The form uses Formspree (free tier):
1. Create account at https://formspree.io
2. Create new form
3. Replace `YOUR_FORM_ID` in the form action:
```html
action="https://formspree.io/f/YOUR_FORM_ID"
```

## 🚀 Performance

### Current Metrics (Estimated)
- Page Size: ~50KB (HTML + CSS + JS)
- Load Time: < 2s on 3G
- Lighthouse Score: 90+

### Optimization Techniques
- Minified CSS/JS (manual)
- Lazy loading images
- Intersection Observer for animations
- Efficient CSS with custom properties
- No external dependencies (except fonts)

## 🐛 Troubleshooting

### Website not loading
1. Check GitHub Pages is enabled
2. Verify DNS records in GoDaddy
3. Wait for DNS propagation (up to 48h)
4. Check browser console for errors

### Language not switching
1. Check `lang/` folder exists with JSON files
2. Verify JavaScript is enabled
3. Check browser console for errors

### Mobile layout broken
1. Check viewport meta tag
2. Verify CSS media queries
3. Test in different browsers

## 📄 License

Proprietary - China Africa Trucks

## 🙏 Credits

- Design: China Africa Trucks Team
- Icons: Font Awesome
- Fonts: Google Fonts (Inter)
- Hosting: GitHub Pages
- Flag Images: flagcdn.com

---

**Last Updated**: 2024-04-11
**Version**: 2.0.0
**Status**: Production Ready ✅

For support or questions, contact: chinaafricatrucks@gmail.com