// C program for Naive Pattern Searching algorithm
#include <stdio.h>
#include <string.h>

void search(char* pat, char* txt){
    int patternLength = strlen(pat);
    int textLength = strlen(txt);


    /* A loop to slide pat[] one by one */
    for (int i = 0; i <= textLength - patternLength; i++) {
        int j;


        /* For current index i, check for pattern match */
        for (j = 0; j < patternLength; j++)
            if (txt[i + j] != pat[j])
                break;

        if (j == patternLength) // if pat[0...patternLength-1] = txt[i, i+1, ...i+patternLength-1]
            printf("Pattern found at index %d \n", i);


    }
}

/* Driver program to test above function */
int main(){
    char txt[] = "sexyboiisviralisasexyboi";
    char pat[] = "boi";
    search(pat, txt);
    return 0;
}
