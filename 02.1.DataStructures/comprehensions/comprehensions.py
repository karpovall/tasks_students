import typing as tp


def get_unique_page_ids(records: list[tp.Mapping[str, tp.Any]]) -> set[int]:
    """
    Get unique web pages visited
    :param records: records of hit-log
    :return: Unique web pages
    """

    return {records[i]['PageID'] for i in range(0, len(records))}


def get_unique_page_ids_visited_after_ts(records: list[tp.Mapping[str, tp.Any]], ts: int) -> set[int]:
    """
    Get unique web pages visited after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :return: Unique web pages visited in hit-log after some timestamp
    """
    return {records[i]['PageID'] for i in range(0, len(records)) if records[i]['EventTime'] > ts}


def get_unique_user_ids_visited_page_after_ts(
        records: list[tp.Mapping[str, tp.Any]],
        ts: int,
        page_id: int
) -> set[int]:
    """
    Get unique users visited given web page after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :param page_id: web page identifier
    :return: Unique users visited given web page after some timestamp
    """

    return {records[i]['UserID'] for i in range(0, len(records)) if
            records[i]['EventTime'] > ts and records[i]['PageID'] == page_id}


def get_events_by_device_type(
        records: list[tp.Mapping[str, tp.Any]],
        device_type: str
) -> list[tp.Mapping[str, tp.Any]]:
    """
    Filter events for given device type with order preservation
    :param records: records of hit-log
    :param device_type: device typy name to filter by
    :return: filtered events
    """

    return [records[i] for i in range(0, len(records)) if records[i]['DeviceType'] == "Internet Explorer"]


DEFAULT_REGION_ID = 100500


def get_region_ids_with_none_replaces_by_default(
        records: list[tp.Mapping[str, tp.Any]]
) -> list[int]:
    """
    Extract visited regions with order preservation. If region not defined, replace it by default region id
    :param records: records of hit-log
    :return: region ids
    """

    return [records[i]['RegionID'] if records[i]['RegionID'] is not None else DEFAULT_REGION_ID for i in
            range(0, len(records))]


def get_region_id_if_not_none(
        records: list[tp.Mapping[str, tp.Any]]
) -> list[int]:
    """
    Extract visited regions if they are defined with order preservation
    :param records: records of hit-log
    :return: region ids
    """

    return [records[i]['RegionID'] for i in range(0, len(records)) if records[i]['RegionID'] is not None]


def get_keys_where_value_is_not_none(r: tp.Mapping[str, tp.Any]) -> list[str]:
    """
    Extract keys where values are defined
    :param r: record of hit-log
    :return: keys where values are defined
    """

    return [i for i in r.keys() if r[i] is not None]


def get_record_with_none_if_key_not_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
) -> dict[str, tp.Any]:
    """
    Get record with other keys replaced by None
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: record with other keys replaced by None
    """

    return {i: r[i] if i in keys else None for i in r.keys()}


def get_record_with_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
) -> dict[str, tp.Any]:
    """
    Filter record by keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered record
    """

    return {i: r[i] for i in keys}

def get_keys_if_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
) -> set[str]:
    """
    Filter keys from record by given keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered keys
    """

    return {i for i in r.keys() if i in keys }
