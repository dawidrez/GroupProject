import globals from 'globals';
import pluginJs from '@eslint/js';
import tseslint from 'typescript-eslint';
import pluginReact from 'eslint-plugin-react';

/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files: ['**/*.{js,mjs,cjs,ts,jsx,tsx}'],
    languageOptions: {
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
  },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  pluginReact.configs.flat.recommended,
  {
    rules: {
      'semi': ['error', 'always'],               // Ensure semicolons at the end of statements
      'quotes': ['error', 'single'],              // Enforce single quotes for strings
      'no-multiple-empty-lines': ['error', { 'max': 1 }],  // Max 1 empty line allowed
      'no-trailing-spaces': 'error',             // Disallow trailing spaces
      'no-unused-vars': ['warn'],                // Warn for unused variables
      'indent': ['error', 2],                    // Enforce 2-space indentation
      'space-before-blocks': ['error', 'always'], // Ensure space before blocks (if, function, etc.)
      'eol-last': ['error', 'always'],           // Ensure a newline at the end of the file
      'comma-dangle': ['error', 'always-multiline'],  // Ensure trailing commas where necessary
      'no-console': 'warn',                      // Warn about console.log statements
      'no-debugger': 'warn',                     // Warn about debugger statements
      'space-infix-ops': 'error',                // Enforce spacing around operators (e.g., `a + b`)
    },
    settings: {
      react: {
        version: 'detect',
      },
    },
  },
];
