/*Algorithm given in the CLRS book */
#include<stdio.h>
#include<string.h>
// d is the number of characters in input alphabet
#define d 256
/* pat -> pattern
    txt -> text
    q -> A prime number
*/
void search(char pat[], char txt[], int q){
    int lengthOfPattern = strlen(pat);
    int lengthOfText = strlen(txt);
    int i, j;
    int patternHash = 0; // hash value for pattern
    int textHash = 0; // hash value for txt
    int h = 1;

    // The value of h would be "pow(d, lengthOfPattern-1)%q"
    for (i = 0; i < lengthOfPattern-1; i++)
        h = (h*d)%q; // d is the number of characters in input alphabet
    // Calculate the hash value of pattern and first window of text
    for (i = 0; i < lengthOfPattern; i++){
        patternHash = (d*patternHash + pat[i])%q;
        textHash = (d*textHash + txt[i])%q;
    }


    // Slide the pattern over text one by one
    for (i = 0; i <= lengthOfText - lengthOfPattern; i++){


        /* Check the hash values of current window of text and pattern. If the
        hash values match then only check for characters on by one*/
        if ( patternHash == textHash ){
            /* Check for characters one by one */
            for (j = 0; j < lengthOfPattern; j++){
                if (txt[i+j] != pat[j])
                    break;
            }
            // if patternHash == textHash and pat[0...lengthOfPattern-1] = txt[i, i+1, ...i+lengthOfPattern-1]
            if (j == lengthOfPattern)
                printf("Pattern found at index %d \n", i);
        }//End of Parent If


        // Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if ( i < lengthOfText-lengthOfPattern ){
            textHash = (d* (textHash - txt[i] * h) + txt[i+lengthOfPattern] )%q;
            if (textHash < 0)// We might get negative value of textHash, converting it to positive
              textHash = (textHash + q);
        }//End of If
    }//End of Parent For


}//End of function Search

/* Driver program to test above function */
int main(){
    char txt[] = "viral is a sexy boi";
    char pat[] = "sexy";
    int q = 101; // A prime number
    search(pat, txt, q);
    return 0;
}
