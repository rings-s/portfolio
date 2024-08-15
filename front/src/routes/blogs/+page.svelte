<script>
    import { BlogStore } from './../../BlogStore';

    let handleClick = () => BlogStore.update(prev => {
        let newBlog = { id: 3, title: 'Drive', description: 'Nicolas Winding Refn', created_at: '2022-01-01' };
        return [...prev, newBlog];
    });
</script>

<div class="max-w-3xl mx-auto p-4 bg-white shadow rounded-lg">
    {#each $BlogStore as blog}
        <div class="my-4 p-5 border-b last:border-b-0">
            <h1 class="text-2xl font-bold text-gray-900">{blog.title}</h1>
            <p class="text-gray-600">{blog.description}</p>
            <p class="text-sm text-gray-400">{blog.created_at}</p>
        </div>
    {/each}

    <button type="button" class="px-4 py-2 mt-3 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-md shadow" on:click={handleClick}>
        Add a Blog
    </button>
</div>
