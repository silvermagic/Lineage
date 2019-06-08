//
// Created by 范炜东 on 2019/5/16.
//

#include <thread>
#include <random>
#include <sstream>
#include <iomanip>

int random(int n) {
  static thread_local std::random_device seed;
  static thread_local std::mt19937 generator(seed());
  thread_local std::uniform_int_distribution<int> distribution;
  return distribution(generator, std::uniform_int_distribution<int>::param_type{0, n});
}

std::string bytes_to_str(const char* buffer, int len)
{
  std::stringstream ss;
  for (int k = 0, j = 0; k < len; k++)
  {
    // 打印起始字节号
    if (!(j % 16))
      ss << std::setfill('0') << std::setw(4) << std::hex << static_cast<int>(k) << ": ";
    // 十六进制打印bytes数据
    ss << std::setfill('0') << std::setw(2) << std::hex << (static_cast<int>(buffer[k]) & 0xFF) << " ";
    j++;
    // 每行打印16个
    if (j != 16)
      continue;

    // ascii打印bytes数据
    ss << "   ";
    int m = k - 15;
    for (size_t n = 0; n < 16; n++)
    {
      char c = *(reinterpret_cast<char const *>(&buffer[m]));
      m++;
      if (c > 31 && c < 128)
        ss << c;
      else
        ss << ".";
    }
    ss << std::endl;
    j = 0;
  }

  // 如果最后一次不足16个需要单独处理
  int last = len % 16;
  if (last)
  {
    // 用空格代替原本需要打印的十六进制bytes数据
    for (int j = 0; j < (16 - last); j++)
      ss << "     ";
    // ascii打印bytes数据
    ss << "   ";
    int k = len - last;
    for (int n = 0; n < last; n++)
    {
      char c = *(reinterpret_cast<char const *>(&buffer[k]));
      k++;
      if (c > 31 && c < 128)
        ss << c;
      else
        ss << ".";
    }
    ss << std::endl;
  }
  return ss.str();
}