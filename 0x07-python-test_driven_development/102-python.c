#include <Python.h>
#include <wchar.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
	const wchar_t *wstr;
	Py_ssize_t length;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p)) {
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_READY(p) != 0) {
		printf("  [ERROR] Failed to get string info\n");
		return;
	}

	wstr = PyUnicode_AsWideCharString(p, &length);
	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", wstr);

	PyMem_Free((void *)wstr);
}
