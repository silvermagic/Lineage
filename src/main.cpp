#include "model/TObject.h"
#include "configure/TConfig.h"
#include "foundation/TLog.hpp"
#include "foundation/TException.hpp"

int main()
{
  TObject obj;
  TConfig cfg;
  Lineage::log::TLog log("main");
  log.log(Lineage::log::severity_level::normal, "%s", "test");
  try
  {
    //throw Lineage::execption::TExecption(Lineage::execption::exceptTag::normal, "test");
    throw Lineage::execption::TExecption("test");
  }
  catch(std::exception &e)
  {
    std::cout<< e.what() << std::endl;
  }
  catch(...)
  {

  }
  return 0;
}
