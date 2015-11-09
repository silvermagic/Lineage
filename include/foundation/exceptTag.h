#ifndef EXCEPTTAG_H_INCLUDED
#define EXCEPTTAG_H_INCLUDED

namespace Lineage{ namespace execption {

enum exceptTag
{
  normal
};

std::map<exceptTag, std::string>::value_type exceptFormat[] = {
  std::map<exceptTag, std::string>::value_type(normal, "%s")
};

}}
#endif // EXCEPTTAG_H_INCLUDED
