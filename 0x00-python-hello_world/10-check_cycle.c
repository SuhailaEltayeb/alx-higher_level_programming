#include "lists.h"

/**
 * check_cycle - function to check if the linked list has cylcle
 * @list: the linked list
 * Return: if there is no cyle, 0, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;
	if (!list || !list->next)
		return(0);
	x = list;
	y = list;
	while (x != NULL && y != NULL && x->next != NULL)
	{
		y = y->next;
		x = x->next->next;
		if (y == x)
		{
			return (1);
		}
	}
	return (0);
}
