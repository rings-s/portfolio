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

<div class="max-w-6xl mx-auto p-5">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each $TestimonialStore as testimonial}
            <div class="bg-white shadow-lg rounded-lg p-6 flex flex-col justify-between">
                <div>
                    <h1 class="text-xl font-bold text-gray-900">{testimonial.client_name}</h1>
                    <p class="text-gray-700">{testimonial.project_name}</p>
                    <p class="text-sm text-gray-500">{testimonial.date}</p>
                    <p class="text-gray-600 mt-2">{testimonial.testimonial_body}</p>
                </div>
            </div>
        {/each}
    </div>

    <button type="button" class="px-6 py-2 mt-6 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-md transition-colors" on:click={handleClick}>
        Add a Testimonial
    </button>
</div>
