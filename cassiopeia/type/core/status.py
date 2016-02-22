import datetime

import cassiopeia.type.core.common
import cassiopeia.type.dto.status


@cassiopeia.type.core.common.inheritdocs
class Shard(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.Shard

    def __str__(self):
        return self.name

    @property
    def host_name(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.hostname

    @property
    def locales(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.locales

    @property
    def name(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.name

    @property
    def platform(self):
        """
        Returns:
            str: the domain name of the server
        """
        return cassiopeia.type.core.common.Platform(self.data.region_tag.upper()) if self.data.region_tag else None

    @property
    def region(self):
        """
        Returns:
            str: the domain name of the server
        """
        return cassiopeia.type.core.common.Region(self.data.slug.upper()) if self.data.slug else None


@cassiopeia.type.core.common.inheritdocs
class ShardStatus(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.ShardStatus

    def __str__(self):
        return "Status ({name})".format(name=self.name)

    def __iter__(self):
        return iter(self.services)

    def __len__(self):
        return len(self.services)

    def __getitem__(self, index):
        return self.services[index]

    @property
    def host_name(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.hostname

    @property
    def locales(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.locales

    @property
    def name(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.name

    @property
    def platform(self):
        """
        Returns:
            str: the domain name of the server
        """
        return cassiopeia.type.core.common.Platform(self.data.region_tag.upper()) if self.data.region_tag else None

    @cassiopeia.type.core.common.lazyproperty
    def services(self):
        """
        Returns:
            str: the domain name of the server
        """
        return [Service(service) for service in self.data.services]

    @property
    def region(self):
        """
        Returns:
            str: the domain name of the server
        """
        return cassiopeia.type.core.common.Region(self.data.slug.upper()) if self.data.slug else None


@cassiopeia.type.core.common.inheritdocs
class Service(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.Service

    def __str__(self):
        return self.name

    def __iter__(self):
        return iter(self.incidents)

    def __len__(self):
        return len(self.incidents)

    def __getitem__(self, index):
        return self.incidents[index]

    @cassiopeia.type.core.common.lazyproperty
    def incidents(self):
        """
        Returns:
            str: the domain name of the server
        """
        return [Incident(incident) for incident in self.data.incidents]

    @property
    def name(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.name

    @property
    def slug(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.slug

    @property
    def status(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.status


@cassiopeia.type.core.common.inheritdocs
class Incident(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.Incident

    def __str__(self):
        return "Incident #{id_}".format(id_=self.id)

    def __iter__(self):
        return iter(self.updates)

    def __len__(self):
        return len(self.updates)

    def __getitem__(self, index):
        return self.updates[index]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return hash(self.id)

    @property
    def active(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.active

    @cassiopeia.type.core.common.lazyproperty
    def created(self):
        """
        Returns:
            str: the domain name of the server
        """
        return datetime.datetime.strptime(self.data.created_at, "%Y-%m-%dT%H:%M:%SZ") if self.data.created_at else None

    @property
    def id(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.id

    @cassiopeia.type.core.common.lazyproperty
    def updates(self):
        """
        Returns:
            str: the domain name of the server
        """
        return [Message(update) for update in self.data.updates]


@cassiopeia.type.core.common.inheritdocs
class Message(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.Message

    def __str__(self):
        return self.content

    def __iter__(self):
        return iter(self.translations)

    def __len__(self):
        return len(self.translations)

    def __getitem__(self, index):
        return self.translations[index]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return hash(self.id)

    @property
    def author(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.author

    @property
    def content(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.content

    @cassiopeia.type.core.common.lazyproperty
    def created(self):
        """
        Returns:
            str: the domain name of the server
        """
        return datetime.datetime.strptime(self.data.created_at, "%Y-%m-%dT%H:%M:%SZ") if self.data.created_at else None

    @property
    def id(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.id

    @property
    def severity(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.severity

    @cassiopeia.type.core.common.lazyproperty
    def translations(self):
        """
        Returns:
            str: the domain name of the server
        """
        return {translation.locale: Translation(translation) for translation in self.data.translations}

    @cassiopeia.type.core.common.lazyproperty
    def updated(self):
        """
        Returns:
            str: the domain name of the server
        """
        return datetime.datetime.strptime(self.data.updated_at, "%Y-%m-%dT%H:%M:%SZ") if self.data.updated_at else None


@cassiopeia.type.core.common.inheritdocs
class Translation(cassiopeia.type.core.common.CassiopeiaObject):
    dto_type = cassiopeia.type.dto.status.Translation

    def __str__(self):
        return self.content

    @property
    def content(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.content

    @property
    def locale(self):
        """
        Returns:
            str: the domain name of the server
        """
        return self.data.locale

    @cassiopeia.type.core.common.lazyproperty
    def updated(self):
        """
        Returns:
            str: the domain name of the server
        """
        return datetime.datetime.strptime(self.data.updated_at, "%Y-%m-%dT%H:%M:%SZ") if self.data.updated_at else None


###############################
# Dynamic SQLAlchemy bindings #
###############################
def _sa_rebind_all():
    Shard.dto_type = cassiopeia.type.dto.status.Shard
    ShardStatus.dto_type = cassiopeia.type.dto.status.ShardStatus
    Service.dto_type = cassiopeia.type.dto.status.Service
    Incident.dto_type = cassiopeia.type.dto.status.Incident
    Message.dto_type = cassiopeia.type.dto.status.Message
    Translation.dto_type = cassiopeia.type.dto.status.Translation
