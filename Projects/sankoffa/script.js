document.addEventListener('DOMContentLoaded', () =>{
    const scenes = document.querySelectorAll('.scene');

    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.6
    }

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            const audio = entry.target.querySelector('audio');

            if (entry.isIntersecting) {
                audio.play()
            } else {
                audio.pause();
                audio.currentTime = 0; // Reset audio to start
            }
        });
    }, options);
    scenes.forEach(scene => {
        observer.observe(scene);
    });
});