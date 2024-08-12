<script>
	import { ProjectStore } from './../../ProjectStore.js';



    let handleClick = () => ProjectStore.update( prev => {
        let newProject = {id:3, name:'Drive', description: 'Nicolas Winding Refn', created_at: '2022-01-01', client: 'Nicolas', end_date: '2022-01-01' }
        return [...prev, newProject]
    })
    
</script>





<div>

    {#each $ProjectStore as project}
        <div>
            <h1>{project.name}</h1>
            <p>{project.description}</p>
            <p>{project.created_at}</p>
            <p>{project.client}</p>
            <p>{project.end_date}</p>
        </div>
    {/each}

  
    <button type="button" class="px-4 py-1 mt-3 border border-gray-100  bg-gray-800 text-white rounded-2xl " on:click={handleClick}>
        ADD A a projcet
    </button>
</div>
