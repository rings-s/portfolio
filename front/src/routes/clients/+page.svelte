<script>
	import { ClientStore } from './../../ClientStore';


    let handleClick = () => BlogStore.update(prev => {
        let newClient = { id: 3, name: 'Drive', phone_number: '123456789', created_at: '2022-01-01' };
        return [...prev, newClient];
    });
</script>




<div>

    {#each $ClientStore as client}
        <div>
            <h1>{client.name}</h1>
            <p>{client.phone_number}</p>
            <p>{client.created_at}</p>
        </div>
    {/each}


    <button type="button" class="px-4 py-1 mt-3 border border-gray-100 bg-gray-800 text-white rounded-2xl" on:click={handleClick}>
        Add a Client
    </button>
</div>
