#include <stdio.h>

int main() {
    char *ptr = NULL; // 포인터를 NULL로 초기화

    // NULL 포인터를 역참조(디레퍼런스)하려고 시도
    *ptr = 'A';

    return 0;
}

