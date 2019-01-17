//
// Created by 范炜东 on 2018/11/16.
//

#include <utility>
#include <string>
#include "ClientPacket.h"

namespace Lineage {

ClientPacket::ClientPacket(std::vector<char> &data)
{
    data_.swap(data);
    opcode_ = (unsigned int)data_[0] & 0xFF;
    offset_ = 1;
}

unsigned int ClientPacket::getOpcode()
{
    return opcode_;
}

std::vector<char> ClientPacket::readBytes()
{
    std::vector<char> v(data_.begin() + offset_, data_.end());
    offset_ = data_.size() + 1;
    return std::move(v);
}

unsigned int ClientPacket::readC()
{
    unsigned int i = (unsigned int)data_[offset_++] & 0xFF;
    return i;
}

unsigned int ClientPacket::readCH()
{
    unsigned int i = (unsigned int)data_[offset_++] & 0xFF;
    i |= data_[offset_++] << 8 & 0xFF00;
    i |= data_[offset_++] << 16 & 0xFF0000;
    return i;
}

unsigned int ClientPacket::readD()
{
    unsigned int i = (unsigned int)data_[offset_++] & 0xFF;
    i |= data_[offset_++] << 8 & 0xFF00;
    i |= data_[offset_++] << 16 & 0xFF0000;
    i |= data_[offset_++] << 24 & 0xFF000000;
    return i;
}

double ClientPacket::readF()
{
    unsigned long long i = (unsigned long long)data_[offset_++] & 0xFFL;
    i |= (unsigned long long)data_[offset_++] << 8 & 0xFF00L;
    i |= (unsigned long long)data_[offset_++] << 16 & 0xFF0000L;
    i |= (unsigned long long)data_[offset_++] << 24 & 0xFF000000L;
    i |= (unsigned long long)data_[offset_++] << 32 & 0xFF00000000L;
    i |= (unsigned long long)data_[offset_++] << 40 & 0xFF0000000000L;
    i |= (unsigned long long)data_[offset_++] << 48 & 0xFF000000000000L;
    i |= (unsigned long long)data_[offset_++] << 56 & 0xFF00000000000000L;
    return *reinterpret_cast<double *>(&i);
}

unsigned int ClientPacket::readH()
{
    unsigned int i = (unsigned int)data_[offset_++] & 0xFF;
    i |= data_[offset_++] << 8 & 0xFF00;
    return i;
}

std::string ClientPacket::readS()
{
    std::string s(data_.data() + offset_);
    offset_ += s.length() + 1;
    return std::move(s);
}

}