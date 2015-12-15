#include <iostream>
#include "model/TObject.h"
#include "configure/TConfig.h"
#include "Poco/Util/PropertyFileConfiguration.h"
#include "Poco/Util/LoggingConfigurator.h"

using Poco::Util::PropertyFileConfiguration;
using Poco::Util::LoggingConfigurator;

int main()
{
  TObject obj;
  Poco::AutoPtr<PropertyFileConfiguration> pcfg =  new PropertyFileConfiguration("./log.properties");
  LoggingConfigurator logcfg;
  logcfg.configure(pcfg);
  try
  {
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
