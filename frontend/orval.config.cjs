module.exports = {
	default: {
		input: {
			target: 'http://localhost:8000/openapi.json'
		},
		output: {
			target: './src/lib/api/gen',
			schemas: './src/lib/api/gen/model',
			client: 'axios',
			mode: 'split',
			clean: true,
			baseUrl: 'http://localhost:8000'
		}
	}
};
