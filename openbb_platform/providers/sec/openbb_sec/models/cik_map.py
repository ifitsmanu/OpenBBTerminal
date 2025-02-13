"""SEC CIK Mapping Model."""

from typing import Any, Dict, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cik_map import CikMapData, CikMapQueryParams
from openbb_sec.utils.helpers import symbol_map


class SecCikMapQueryParams(CikMapQueryParams):
    """SEC CIK Mapping Query.

    Source: https://sec.gov/
    """


class SecCikMapData(CikMapData):
    """SEC CIK Mapping Data."""


class SecCikMapFetcher(
    Fetcher[
        SecCikMapQueryParams,
        SecCikMapData,
    ]
):
    """Transform the query, extract and transform the data from the SEC endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SecCikMapQueryParams:
        """Transform the query."""
        return SecCikMapQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SecCikMapQueryParams,  # pylint: disable=W0613:unused-argument
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> Dict:
        """Return the raw data from the SEC endpoint."""
        results = {"cik": symbol_map(query.symbol)}
        if not results:
            return {"Error": "Symbol not found."}
        return results

    @staticmethod
    def transform_data(
        query: SecCikMapQueryParams, data: Dict, **kwargs: Any
    ) -> SecCikMapData:
        """Transform the data to the standard format."""
        return SecCikMapData.model_validate(data)
