import datetime

import luigi

from serenity.equity.batch.load_sharadar_corp_actions import LoadCorporateActionsTask
from serenity.equity.batch.load_sharadar_event_calendar import LoadEventCalendarTask
from serenity.equity.batch.load_sharadar_fundamentals import LoadEquityFundamentalsTask
from serenity.equity.batch.load_sharadar_insider_holdings import LoadInsiderHoldingsTask
from serenity.equity.batch.load_sharadar_institutional_holdings import LoadInstitutionalHoldingsTask
from serenity.equity.batch.load_sharadar_meta import LoadSharadarMetaTask
from serenity.equity.batch.load_sharadar_prices import LoadEquityPricesTask
from serenity.equity.batch.load_sharadar_tickers import LoadSharadarTickersTask


class SharadarDailyDownloadTask(luigi.WrapperTask):
    start_date = luigi.DateParameter(default=datetime.date.today())
    end_date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        yield LoadSharadarMetaTask()
        yield LoadSharadarTickersTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadCorporateActionsTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadEventCalendarTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadEquityPricesTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadEquityFundamentalsTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadInsiderHoldingsTask(start_date=self.start_date, end_date=self.end_date)
        yield LoadInstitutionalHoldingsTask(start_date=self.start_date, end_date=self.end_date)


if __name__ == '__main__':
    luigi.build([SharadarDailyDownloadTask()], local_scheduler=True)
