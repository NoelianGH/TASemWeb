// Basic JavaScript for Semantic Web Template

document.addEventListener('DOMContentLoaded', function() {
    console.log('Semantic Web Template loaded');

    // Example: Extract structured data from JSON-LD
    const jsonLdScript = document.querySelector('script[type="application/ld+json"]');
    if (jsonLdScript) {
        try {
            const structuredData = JSON.parse(jsonLdScript.textContent);
            console.log('Structured Data:', structuredData);
        } catch (e) {
            console.error('Error parsing JSON-LD:', e);
        }
    }

    // Example: Simple navigation highlight
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Example: Demonstrate RDFa data extraction (simplified)
    const elementsWithProperty = document.querySelectorAll('[property]');
    console.log('RDFa properties found:', elementsWithProperty.length);
});