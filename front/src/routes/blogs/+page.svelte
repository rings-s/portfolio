<script>
    import { BlogStore } from './../../BlogStore';

    let handleClick = () => BlogStore.update(prev => {
        let newBlog = { id: 3, title: 'Drive', description: 'Nicolas Winding Refn', created_at: '2022-01-01' };
        return [...prev, newBlog];
    });
</script>

<div>
    {#each $BlogStore as blog}
        <div>
            <h1>{blog.title}</h1>
            <p>{blog.description}</p>
            <p>{blog.created_at}</p>
            
        </div>
    {/each}

    <button type="button" class="px-4 py-1 mt-3 border border-gray-100 bg-gray-800 text-white rounded-2xl" on:click={handleClick}>
        Add a Blog
    </button>
</div>
