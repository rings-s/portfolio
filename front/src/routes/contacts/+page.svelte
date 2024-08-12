<script>
    import { ContactStore } from './../../ContactStore';



    let handleClick = () => ContactStore.update(prev => {
        let newContact = { id: 3, name: 'Drive', email: '123456789', message: 'Nicolas Winding Refn', created_at: '2022-01-01' };
        return [...prev, newContact];
    });
</script>




<div>

    {#each $ContactStore as contact}
        <div>
            <h1>{contact.name}</h1>
            <p>{contact.email}</p>
            <p>{contact.message}</p>
        </div>
    {/each}


    <button type="button" class="px-4 py-1 mt-3 border border-gray-100 bg-gray-800 text-white rounded-2xl" on:click={handleClick}>
        Add a Contact
    </button>
    
</div>
