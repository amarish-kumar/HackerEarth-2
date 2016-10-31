#include <iostream>
using namespace std;

void bubble_sort(int A[], int n, int k);

int main() {
    int N, K, ai;
    cin >> N >> K;
    int A[N];
    for(int i = 0; i < N; i++) {
        cin >> ai;
        A[i] = ai;
    }

    bubble_sort(A, N, K);
    int i;
    for(i = 0; i < N-1; i++) {
        cout << A[i] << " ";
    }
    cout << A[i] << endl;

    return 0;
}

void bubble_sort(int A[], int n, int k){
    int temp; 
    for(int w = 0; w < n-1; w++) {
        for(int i = 0; i < n-w-1; i++){
            if(A[i] % k > A[i+1] % k) {
                temp = A[i];
                A[i] = A[i+1];
                A[i+1] = temp;
            }
        }
    }
}
