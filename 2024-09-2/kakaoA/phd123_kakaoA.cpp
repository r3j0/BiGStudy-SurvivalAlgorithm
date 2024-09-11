#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
using namespace std;


int solution(vector<string> friends, vector<string> gifts) {
    int cnt = 0;
    int table[50][50] = {0};
    unordered_map<string, int> pindex;
    unordered_map<string, int> gift_rate;
    unordered_map<string, int> cnt_gift;
    for(const string& s : friends) {
    	pindex.insert(make_pair(s, cnt++));
    	cnt_gift.insert(make_pair(s, 0));
	}
	for(const string& gift : gifts) {
		istringstream ss(gift);
		string from, to;
		getline(ss, from, ' ');
		getline(ss, to, ' ');
		table[pindex.find(from)->second][pindex.find(to)->second]++;
	}
	
	for(vector<string>::iterator it1 = friends.begin(); it1 != friends.end(); it1++) {
		for(vector<string>::iterator it2 = it1 + 1; it2 != friends.end(); it2 ++) {
			int give = 0, get = 0;
			give = table[pindex.find(*it1)->second][pindex.find(*it2)->second];
			get = table[pindex.find(*it2)->second][pindex.find(*it1)->second];
			if(give > get) {
				cnt_gift[*it1]++;
			}
			else if(give < get) {
				cnt_gift[*it2]++;
			}
			else {
				int total_give1 = 0, total_get1 = 0;
				for(int i=0; i<friends.size(); i++) {
					total_give1 += table[pindex.find(*it1)->second][i];
				}
				for(int i=0; i<friends.size(); i++) {
					total_get1 += table[i][pindex.find(*it1)->second];
				}
				
				int total_give2 = 0, total_get2 = 0;
				for(int i=0; i<friends.size(); i++) {
					total_give2 += table[pindex.find(*it2)->second][i];
				}
				for(int i=0; i<friends.size(); i++) {
					total_get2 += table[i][pindex.find(*it2)->second];
				}
				
				if(total_give1-total_get1 > total_give2-total_get2) {
					cnt_gift[*it1]++;
				}
				else if(total_give1-total_get1 < total_give2-total_get2) {
					cnt_gift[*it2]++;
				}
			}
		}
	}
	
	int max = -1;
	for(const string& s : friends) {
		if(cnt_gift[s] > max) {
			max = cnt_gift[s];
		}
	}
    
    return max;
}

int main()
{
	int sel, res;
	vector<string> friends, gifts;
	printf("1. \nfriends : %s,\ngifts : %s\n", "[\"muzi\", \"ryan\", \"frodo\", \"neo\"]", "[\"muzi frodo\", \"muzi frodo\", \"ryan muzi\", \"ryan muzi\", \"ryan muzi\", \"frodo muzi\", \"frodo ryan\", \"neo muzi\"]");
	printf("2. \nfriends : %s,\ngifts : %s\n", "[\"joy\", \"brad\", \"alessandro\", \"conan\", \"david\"]", "[\"alessandro brad\", \"alessandro joy\", \"alessandro conan\", \"david alessandro\", \"alessandro david\"]");
	printf("3. \nfriends : %s,\ngifts : %s\n", "[\"a\", \"b\", \"c\"]", "[\"a b\", \"b a\", \"c a\", \"a c\", \"a c\", \"c a\"]");
	
	printf("<select> : ");
	cin >> sel;
	
	switch(sel) {
	case 1:
		friends.push_back("muzi");
		friends.push_back("ryan");
		friends.push_back("frodo");
		friends.push_back("neo");
		gifts.push_back("muzi frodo");
		gifts.push_back("muzi frodo");
		gifts.push_back("ryan muzi");
		gifts.push_back("ryan muzi");
		gifts.push_back("ryan muzi");
		gifts.push_back("frodo muzi");
		gifts.push_back("frodo ryan");
		gifts.push_back("neo muzi");
		res = solution(friends, gifts);
		cout << "<result> : " << res << '\n';
	break;
	case 2:
		friends.push_back("joy");
		friends.push_back("brad");
		friends.push_back("alessandro");
		friends.push_back("conan");
		friends.push_back("david");
		gifts.push_back("alessandro brad");
		gifts.push_back("alessandro joy");
		gifts.push_back("alessandro conan");
		gifts.push_back("david alessandro");
		gifts.push_back("alessandro david");
		res = solution(friends, gifts);
		cout << "<result> : " << res << '\n';
	break;
	case 3:
		friends.push_back("a");
		friends.push_back("b");
		friends.push_back("c");
		gifts.push_back("a b");
		gifts.push_back("b a");
		gifts.push_back("c a");
		gifts.push_back("a c");
		gifts.push_back("a c");
		gifts.push_back("c a");
		res = solution(friends, gifts);
		cout << "<result> : " << res << '\n';
	break;
	default:
	break;
	}
	
	
	return 0;
}
