#include <iostream>
#include "model/TObject.h"
#include "configure/TConfig.h"
#include "Poco/Util/PropertyFileConfiguration.h"
#include "Poco/Util/LoggingConfigurator.h"
#include "L1DatabaseFactory.h"
//#include "utils/TPerformanceTimer.h"

using Poco::Util::PropertyFileConfiguration;
using Poco::Util::LoggingConfigurator;

TConfig CONFIG;

int main()
{
	try
	{
		TObject obj;
		Poco::AutoPtr<PropertyFileConfiguration> pcfg =  new PropertyFileConfiguration("./config/log.properties");
		LoggingConfigurator logcfg;
		logcfg.configure(pcfg);
		CONFIG.load();

    Poco::Data::Session ses = L1DatabaseFactory::getInstance().getConnection();
		/*std::cout << cfg.PRINCE_MAX_HP << std::endl;

    TPerformanceTimer timer;
    sleep(2);
    std::cout << "完成!\t\t耗时: " << timer.elapsedTimeMillis() << "\t毫秒" << std::endl;*/
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
