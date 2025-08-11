#include <stdio.h>


int isPowerOfTwo(int n) {
    return (n > 0 && (n & (n - 1)) == 0);
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int A, B;
        scanf("%d %d", &A, &B);

        if (A == B) {
            printf("YES\n");
            continue;
        }

        int max = A > B ? A : B;
        int min = A < B ? A : B;

        if (max % min != 0) {
            printf("NO\n");
        } else {
            int ratio = max / min;
            if (isPowerOfTwo(ratio)) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }

    return 0;
}
