const form = document.getElementById("contactForm");
const status = document.getElementById("formStatus");

form.addEventListener("submit", function
    (e) {
        e.preventDefault();
        // simulate sending data
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.getElementById("message").value.trim();
        
        if (name && email && message) {
            //  Simulate form procesing
            setTimeout(() => {
                status.textContent = "Information sent successfully! We will get back to you shortly.";
                status.classList.add("success");
                form.reset();
            }, 500)
        } else {
            status.textContent = "Please fill out all fields.";
            status.classList.remove("success");
            status.classList.add("error");
        }
    });
    
        // Smooth scroll for Navigation links


    // Smooth scroll for Navigation links
    document.querySelectorAll('.nav-list a').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const section = document.querySelector(this.getAttribute('href'));
            section.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Scroll to services when hero button is clicked
    document.querySelector('.hero .btn').addEventListener('click', () => {
       document.querySelector(".services").scrollIntoView({ behavior: 'smooth' });
    });

    // Handle eplore buttons on service section
    