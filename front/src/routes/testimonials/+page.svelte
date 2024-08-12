<script>
    import { TestimonialStore } from './../../TestimonialStore';

    let handleClick = () => TestimonialStore.update(prev => {
        let newTestimonial = {
            id: prev.length > 0 ? Math.max(...prev.map(t => t.id)) + 1 : 1,
            client_name: 'Drive',
            project_name: 'Nicolas Winding Refn',
            date: '2022-01-01',
            testimonial_body: 'Amazing direction and cinematography.'
        };
        return [...prev, newTestimonial];  
    });
</script>

<div>
    {#each $TestimonialStore as testimonial}
        <div>
            <h1>{testimonial.client_name}</h1>
            <p>{testimonial.project_name}</p>
            <p>{testimonial.date}</p>
            <p>{testimonial.testimonial_body}</p>
        </div>
    {/each}

    <button type="button" class="px-4 py-1 mt-3 border border-gray-100 bg-gray-800 text-white rounded-2xl" on:click={handleClick}>
        Add a Testimonial
    </button>
</div>
