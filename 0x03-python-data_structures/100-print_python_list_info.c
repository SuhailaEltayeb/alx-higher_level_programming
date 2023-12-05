#include <Python.h>
/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: pyobjectnlist
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, reserved, size;
	PyObject *O;

	size = Py_SIZE(p);
	reserved = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", reserved);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		O = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(O)->tp_name);
	}
}
