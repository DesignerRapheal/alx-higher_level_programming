#include "lists.h"

/**
 * insert_node - Inserts items into a sorted list in the appropriate position
 * @head: The address of the list
 * @number: The number to be inserted into the node
 *
 * Return: The address of the new node
 *
 * Author: DesignerRapheal
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (node == NULL || node->n >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
