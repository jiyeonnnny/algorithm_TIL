```cpp
#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main(void) {

	int T, value;
	queue<int> Q;
	string command;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> command;

		if (command == "push") {
			cin >> value;
			Q.push(value);
		}
		else if (command == "pop") {
			if (Q.empty()) cout << -1 << endl;
			else {
				cout << Q.front() << endl;
				Q.pop();
			}
		}
		else if (command == "size") {
			cout << Q.size() << endl;
		}
		else if (command == "empty") {
			cout << Q.empty() << endl;
		}
		else if (command == "front") {
			if (Q.empty()) cout << -1 << endl;
			else cout << Q.front() << endl;
		}
		else {
			if (Q.empty()) cout << -1 << endl;
			else cout << Q.back() << endl;
		}
	}

	return 0;
}

```
