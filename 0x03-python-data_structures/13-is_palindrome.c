#include "lists.h"

/**
 * check - function to check if list is palinndrome
 * @head: linked list head
 * @tail: linked list tail
 * Return: 1
 */
int check(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		 return (1);
	if (check(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		 return (1);
	}
	 return (0);
}
/**
 * is_palindrome - functio to check if list is palindrome ot not
 * @head: linked lidt head
 * Return: if not palindrome, 0, or 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check(head, *head));
}
