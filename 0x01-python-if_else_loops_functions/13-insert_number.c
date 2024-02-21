#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nnejw;

	nnejw = malloc(sizeof(listint_t));
	if (nnejw == NULL)
		return (NULL);
	nnejw->n = number;

	if (node == NULL || node->n >= number)
	{
		nnejw->next = node;
		*head = nnejw;
		return (nnejw);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nnejw->next = node->next;
	node->next = nnejw;

	return (nnejw);
}
