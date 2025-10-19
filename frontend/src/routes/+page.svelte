<script lang="ts">
	import { onMount } from 'svelte';
	import { getFastAPI } from '$lib/api/gen/fastAPI';
	import type { Todo } from '$lib/api/gen/model';

	const api = getFastAPI();

	let todos = $state<Todo[]>([]);
	let newTodoTitle = $state('');
	let loading = $state(false);

	async function loadTodos() {
		loading = true;
		try {
			const response = await api.listTodos();
			todos = response.data;
		} catch (error) {
			console.error('Failed to load todos:', error);
		} finally {
			loading = false;
		}
	}

	async function addTodo() {
		if (!newTodoTitle.trim()) return;

		try {
			const response = await api.createTodo({
				title: newTodoTitle,
				completed: false
			});
			todos = [...todos, response.data];
			newTodoTitle = '';
		} catch (error) {
			console.error('Failed to create todo:', error);
		}
	}

	async function toggleTodo(todo: Todo) {
		try {
			const response = await api.updateTodo(todo.id, {
				completed: !todo.completed
			});
			todos = todos.map((t) => (t.id === todo.id ? response.data : t));
		} catch (error) {
			console.error('Failed to update todo:', error);
		}
	}

	async function removeTodo(id: number) {
		try {
			await api.deleteTodo(id);
			todos = todos.filter((t) => t.id !== id);
		} catch (error) {
			console.error('Failed to delete todo:', error);
		}
	}

	onMount(() => {
		loadTodos();
	});
</script>

<div class="container">
	<h1>Todo List</h1>

	<div class="add-todo">
		<input
			type="text"
			bind:value={newTodoTitle}
			placeholder="What needs to be done?"
			onkeydown={(e) => e.key === 'Enter' && addTodo()}
		/>
		<button onclick={addTodo}>Add</button>
	</div>

	{#if loading}
		<p>Loading...</p>
	{:else if todos.length === 0}
		<p class="empty">No todos yet. Add one above!</p>
	{:else}
		<ul class="todo-list">
			{#each todos as todo (todo.id)}
				<li class:completed={todo.completed}>
					<input type="checkbox" checked={todo.completed} onchange={() => toggleTodo(todo)} />
					<span>{todo.title}</span>
					<button class="delete" onclick={() => removeTodo(todo.id)}> × </button>
				</li>
			{/each}
		</ul>
	{/if}
</div>

<style>
	.container {
		max-width: 600px;
		margin: 2rem auto;
		padding: 2rem;
	}

	h1 {
		text-align: center;
		color: #333;
	}

	.add-todo {
		display: flex;
		gap: 0.5rem;
		margin: 2rem 0;
	}

	input[type='text'] {
		flex: 1;
		padding: 0.75rem;
		border: 2px solid #ddd;
		border-radius: 4px;
		font-size: 1rem;
	}

	button {
		padding: 0.75rem 1.5rem;
		background: #007bff;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		font-size: 1rem;
	}

	button:hover {
		background: #0056b3;
	}

	.todo-list {
		list-style: none;
		padding: 0;
	}

	.todo-list li {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 1rem;
		border-bottom: 1px solid #eee;
	}

	.todo-list li span {
		flex: 1;
	}

	.todo-list li.completed span {
		text-decoration: line-through;
		color: #999;
	}

	.delete {
		background: #dc3545;
		padding: 0.25rem 0.75rem;
		font-size: 1.5rem;
		line-height: 1;
	}

	.delete:hover {
		background: #c82333;
	}

	.empty {
		text-align: center;
		color: #999;
		padding: 2rem;
	}
</style>
