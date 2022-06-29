#include "wsn.h"

int decCalculation(char *c, char *k) {
    int temp;
    if (*c >= 0 && *c <= 26) {
        *c = *c - (*k - 'a');
        if (*c < 0) {
            *c = *c + 'a' + 26;
        } else {
            *c = *c + 'a';
        }
    } else if (*c < 0) {
        temp = *c + MAX;
        *c = temp + (temp * -1) + (temp * -1);
    }
    return *c;
}

/*Vignere cipher decryption*/
int decrypt(struct Msg *msg, char key[73]) {
    int i, j;
    int enc_iteration = ENC_ITERATION;

    for (i = 0; i < 73; i++) {
        for (j = 0; j < ENC_ITERATION; j++) {
            (*msg).ciphertext[i] = decCalculation(&msg->ciphertext[i], &key[i]);
        }
    }
    
    for (i = 0; i < 31; i++) {
        for (j = 0; j < ENC_ITERATION; j++) {
            (*msg).et_ciphertext[i] = decCalculation(&msg->et_ciphertext[i], &key[i]);
        }
    }

    return(0);
}
