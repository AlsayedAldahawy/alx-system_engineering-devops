#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; ++i)
	{
		pid_t child_pid = fork();

		if (child_pid == 0)
		{
			/* Child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0); /* Child process exits immediately */
		}
	}

	infinite_while();

	/* Parent process continues execution */
	return (0);
}
