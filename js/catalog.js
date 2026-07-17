document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn[data-filter]');
    const productCards = document.querySelectorAll('.catalog-card[data-category]');
    const catalogCount = document.getElementById('catalogCount');

    filterButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const filter = button.dataset.filter;
            let visibleCount = 0;

            filterButtons.forEach((item) => {
                const selected = item === button;
                item.classList.toggle('active', selected);
                item.setAttribute('aria-pressed', selected ? 'true' : 'false');
            });

            productCards.forEach((card) => {
                const categories = card.dataset.category.split(' ');
                const visible = filter === 'all' || categories.includes(filter);
                card.hidden = !visible;
                if (visible) visibleCount += 1;
            });

            if (catalogCount) {
                catalogCount.textContent = `${visibleCount} ${visibleCount === 1 ? 'model' : 'models'}`;
            }
        });
    });

    document.querySelectorAll('.quote-product[data-product]').forEach((button) => {
        button.addEventListener('click', () => {
            const product = button.dataset.product;
            const message = `Hello China Africa Trucks, I would like a quotation for the ${product}. Please send available configurations and export options.`;
            window.open(`https://wa.me/2348140067523?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
        });
    });
});
