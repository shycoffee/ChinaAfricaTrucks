/**
 * Internationalization (i18n) Module
 * Supports English (default) and Chinese
 */

const i18n = {
    currentLang: 'en',
    translations: {},
    
    async init() {
        // Load both language files
        await this.loadTranslations('en');
        await this.loadTranslations('zh');
        
        // Check for saved language preference
        const savedLang = localStorage.getItem('language');
        if (savedLang && this.translations[savedLang]) {
            this.currentLang = savedLang;
        }
        
        // Apply initial translation
        this.updatePageLanguage();
        
        // Set up language switcher
        this.setupLanguageSwitcher();
    },
    
    async loadTranslations(lang) {
        try {
            const response = await fetch(`lang/${lang}.json`);
            if (!response.ok) throw new Error(`Failed to load ${lang}.json`);
            this.translations[lang] = await response.json();
        } catch (error) {
            console.error(`Error loading ${lang} translations:`, error);
            // Fallback to empty object
            this.translations[lang] = {};
        }
    },
    
    switchLanguage(lang) {
        if (!this.translations[lang]) {
            console.error(`Language ${lang} not available`);
            return;
        }
        
        this.currentLang = lang;
        localStorage.setItem('language', lang);
        this.updatePageLanguage();
        this.updateHTMLLang();
    },
    
    updatePageLanguage() {
        const texts = this.translations[this.currentLang];
        if (!texts) return;
        
        // Update all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.getNestedValue(texts, key);
            
            if (translation) {
                if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                    element.placeholder = translation;
                } else {
                    element.textContent = translation;
                }
            }
        });
        
        // Update language switcher text
        const langSwitcher = document.getElementById('currentLang');
        if (langSwitcher) {
            langSwitcher.textContent = this.currentLang === 'en' ? '中文' : 'English';
        }
        
        // Update meta tags
        this.updateMetaTags(texts);
    },
    
    updateHTMLLang() {
        document.documentElement.lang = this.currentLang;
    },
    
    updateMetaTags(texts) {
        if (texts.meta) {
            const metaDescription = document.querySelector('meta[name="description"]');
            const metaKeywords = document.querySelector('meta[name="keywords"]');
            const ogTitle = document.querySelector('meta[property="og:title"]');
            const ogDescription = document.querySelector('meta[property="og:description"]');
            
            if (metaDescription && texts.meta.description) {
                metaDescription.setAttribute('content', texts.meta.description);
            }
            if (metaKeywords && texts.meta.keywords) {
                metaKeywords.setAttribute('content', texts.meta.keywords);
            }
            if (ogTitle && texts.meta.title) {
                ogTitle.setAttribute('content', texts.meta.title);
            }
            if (ogDescription && texts.meta.description) {
                ogDescription.setAttribute('content', texts.meta.description);
            }
            
            // Update page title
            if (texts.meta.title) {
                document.title = texts.meta.title;
            }
        }
    },
    
    getNestedValue(obj, path) {
        return path.split('.').reduce((current, key) => {
            return current && current[key] !== undefined ? current[key] : null;
        }, obj);
    },
    
    setupLanguageSwitcher() {
        const switcher = document.getElementById('langSwitch');
        if (switcher) {
            switcher.addEventListener('click', () => {
                const newLang = this.currentLang === 'en' ? 'zh' : 'en';
                this.switchLanguage(newLang);
            });
        }
    },
    
    // Get translation for a specific key
    t(key) {
        const texts = this.translations[this.currentLang];
        if (!texts) return key;
        return this.getNestedValue(texts, key) || key;
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    i18n.init();
});