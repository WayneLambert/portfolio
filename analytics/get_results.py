from json import dump, dumps
from time import perf_counter, sleep
from requests import get

start_time = perf_counter()

packages_url = 'https://formulae.brew.sh/api/formula.json'
req = get(packages_url)
packages_json = req.json()[:5]
packages_str = dumps(packages_json[0], indent=2)


def get_results():
    results = []
    for package in packages_json:
        package_name = package['name']
        package_desc = package['desc']
        package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
        req = get(package_url)
        package_json = req.json()

        installs_30 = (package_json
                    ['analytics']
                    ['install']
                    ['30d']
                    [package_name])

        installs_90 = (package_json
                    ['analytics']
                    ['install']
                    ['90d']
                    [package_name])

        installs_365 = (package_json
                        ['analytics']
                        ['install']
                        ['365d']
                        [package_name])

        data = {
            'name': package_name,
            'desc': package_desc,
            'analytics': {
                '30d': installs_30,
                '90d': installs_90,
                '365d': installs_365,
            }
        }

        results.append(data)
        time_delay = req.elapsed.total_seconds()
        sleep(time_delay)
        print(f'Retrieved {package_name} in {time_delay} seconds')

    end_time = perf_counter()
    print(f'Finished saving {len(results)} packages in {end_time - start_time} seconds')
    return results


results_json = get_results()

with open('package_info.json', 'w') as f:
    dump(results_json, f, indent=2)
