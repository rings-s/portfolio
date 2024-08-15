<script>
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';

	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });
</script>

<div>
	<header class="bg-white shadow-md">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
			<h1 class="text-lg leading-6 font-semibold text-gray-900 my-4">
				<a href="/" class="hover:text-gray-700 transition duration-150 ease-in-out">Ringo</a>
			</h1>

			<nav aria-label="Main navigation">
				<ul class="flex items-center gap-4">
					<li><a href="/" class="text-base text-gray-600 hover:text-gray-900">Home</a></li>
					<li><a href="/about" class="text-base text-gray-600 hover:text-gray-900">About</a></li>
					<li>
						<a href="/services" class="text-base text-gray-600 hover:text-gray-900">Services</a>
					</li>
					<li>
						<a href="/projects" class="text-base text-gray-600 hover:text-gray-900">Projects</a>
					</li>
					<li>
						<a href="/testimonials" class="text-base text-gray-600 hover:text-gray-900"
							>Testimonials</a
						>
					</li>
					<li>
						<a href="/contacts" class="text-base text-gray-600 hover:text-gray-900">Contacts</a>
					</li>
					<li><a href="/blogs" class="text-base text-gray-600 hover:text-gray-900">blogs</a></li>
				</ul>
			</nav>
		</div>
	</header>

	<slot />
</div>
