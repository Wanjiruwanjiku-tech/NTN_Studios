fetch('stories.json')
  .then(response => response.json())
  .then(data => {
    const story = data[0]; // assuming only one story for now
    const container = document.getElementById('blog-container');

    // Create the story layout
    const storyHTML = `
      <div class="story-card">
        <img src="${story.image}" alt="${story.title}" class="story-image" />
        <h2>${story.title}</h2>
        <p><strong>Author:</strong> ${story.author} | <em>${story.date}</em></p>
        <div class="story-content">${marked.parse(story.content)}</div>
      </div>
    `;

    container.innerHTML = storyHTML;
  })
  .catch(error => {
    console.error("Error loading story:", error);
  });
