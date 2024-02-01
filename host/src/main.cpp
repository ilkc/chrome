#include <iostream>
#include <string>
#include <memory>
#include <fstream>
#include <stdint.h>
#include <windows.h>
#include <process.h>

using namespace std;

union U32_U8 {
	uint32_t u32;
	uint8_t u8[4];
} ;

void write_recieved_data(unique_ptr<char[]>& data) {
	const string filename{ "./intput.txt" };

	string msg = data.get() + '\0';
	ofstream wf(filename, fstream::out | fstream::app);
	if (!wf.is_open()) {
		return;
	}

	wf << msg << endl;

	wf.close();
}

int main() {
	constexpr size_t INPUT_DATA_LENGTH = 4;
	size_t inputSize{ 0 };
	U32_U8 lenBuf;
	lenBuf.u32 = 0;
	inputSize = fread(lenBuf.u8, 1, 4, stdin);
	if (inputSize != INPUT_DATA_LENGTH) {
		return 0;
	}
	
	int iLen = (int)lenBuf.u32;
	if (iLen <= 0) {
		return 0;
	}

	unique_ptr<char[]> receivedData = make_unique<char[]>(8 * iLen);
	inputSize = fread(receivedData.get(), 1, iLen, stdin);

	write_recieved_data(receivedData);
	fwrite(lenBuf.u8, 1, 4, stdout);
	fwrite(receivedData.get(), 1, iLen, stdout);
	fflush(stdout);

	Sleep(1000);
	system("python client.py");
	
}
