export function fadein(node: HTMLElement, { duration = 800, delay = 0 }: { duration?: number; delay?: number } = {}) {
    node.style.opacity = '0';
    node.style.transform = 'translateY(20px)';
    node.style.transition = `opacity ${duration}ms ease-out, transform ${duration}ms ease-out`;
    node.style.transitionDelay = `${delay}ms`;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                node.style.opacity = '1';
                node.style.transform = 'translateY(0)';
                observer.unobserve(node);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    observer.observe(node);

    return {
        destroy() {
            observer.disconnect();
        }
    };
}
